class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj_list[pattern].append(word)
        
        q = [beginWord]
        visited = set([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.pop(0)
                visited.add(word)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited: 
                            visited.add(nei)
                            q.append(nei)
            res += 1
        
        return 0
