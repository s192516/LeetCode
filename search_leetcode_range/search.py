import sys
import requests as req

from functools import lru_cache

url = 'https://leetcode-cn.com/graphql'


# 分页加载排名列表
@lru_cache
def loadPage(page):
    query = "{\nlocalRanking(page:" + str(page) + ") {\nrankingNodes {\ncurrentRating\nuser {\nusername\n}\n}\n}\n}\n"
    retry = 0
    while retry < 3:
        resp = req.post(url=url, json={'query': query})
        if resp.status_code == 200:
            nodes = resp.json()['data']['localRanking']['rankingNodes']
            return [(int(nd['currentRating']), nd['user']['username']) for nd in nodes]
        else:
            retry += 1
    return None


# 根据用户名获取其个人主页显示的真实排名
# 排行榜上部分coder没有真实排名，导致排行榜上的排名与个人主页排名并不一致
# 实测LC的计算使用的排名是个人主页的排名
@lru_cache
def getUserRank(uid):
    operationName = "userContest"
    query = "query userContest($userSlug: String!){\n userContestRanking(userSlug: $userSlug){" \
            "\ncurrentRatingRanking\n}\n}\n "
    variables = {'userSlug': uid}
    retry = 0
    while retry < 3:
        resp = req.post(url=url, json={
            'operationName': operationName,
            'query': query,
            'variables': variables
        })
        if resp.status_code == 200:
            ranking = resp.json()['data']['userContestRanking']

            return ranking['currentRatingRanking'] if ranking else None
        else:
            retry += 1
    return None


# 使用二分的方式获取1600分以上的人数，并使用 getUserRank 方法校准
def get1600Count():
    l, r = 1, 1000
    scores = None
    while l < r:
        mid = (l + r) // 2
        scores = loadPage(mid)
        print(f'第 {mid} 页：', scores)
        if not scores:
            return None
        if scores[-1][0] < 1600:
            r = mid
        else:
            l = mid + 1
    print('校准中...')
    while True:
        for (score, uid) in scores[::-1]:
            if score >= 1600:
                ret = getUserRank(uid)
                if ret :
                    return ret
        l -= 1
        scores = loadPage(l)


# 获取指定排名的用户，并使用 getUserRank 方法校准
@lru_cache
def getUser(rank):
    if rank <= 0:
        raise Exception('无效的排名')
    p = (rank - 1) // 25 + 1
    of = (rank - 1) % 25
    scores = loadPage(p)
    if of >= len(scores):
        raise Exception('无效的排名')
    while True:
        ranking = getUserRank(scores[of][1])
        if ranking == rank:
            return scores[of]
        if ranking > rank:
            # 特殊情况，排名很靠后时，顺序是乱的
            for i in [0, 1, -1]:
                if i != 0:
                    scores = loadPage(p + i)
                for _, uid in scores:
                    r = getUserRank(uid)
                    if r == rank:
                        return _, uid
            raise Exception('校准失败')
        if not ranking or ranking < rank:
            of += 1 if not ranking else rank - ranking
        if of >= len(scores):
            p += of // len(scores)
            of %= len(scores)
            scores = loadPage(p)


total = get1600Count()
if not total:
    print('网络故障')
    sys.exit()
print(f'1600 分以上共计 {total} 人')
guardian = int(total * 0.05)
knight = int(total * 0.25)
g_first, g_last = getUser(1), getUser(guardian)
print(f'Guardian(top 5%): 共 {guardian} 名，最低 {g_last[0]} 分（uid: {g_last[1]}），最高 {g_first[0]} 分（uid: {g_first[1]}）')
k_first, k_last = getUser(guardian + 1), getUser(knight)
print(f'Knight(top 25%): 共 {knight} 名，最低 {k_last[0]} 分（uid: {k_last[1]}），最高 {k_first[0]} 分（uid: {k_first[1]}）')
