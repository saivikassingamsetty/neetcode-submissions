from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for word in words:
            for ch in word:
                indegree[ch] = 0

        for i in range(len(words)-1):
            firstWord = words[i]
            secondWord = words[i+1]

            k = 0
            foundDiff = False
            while k < len(firstWord) and k < len(secondWord):
                # first diff character
                if firstWord[k] != secondWord[k]:
                    if secondWord[k] not in graph[firstWord[k]]:
                        graph[firstWord[k]].add(secondWord[k])
                        indegree[secondWord[k]] += 1
                    foundDiff = True
                    break

                k += 1
            
            # prefix
            if not foundDiff and len(firstWord) > len(secondWord):
                return ""
        
        queue = deque()
        
        for ch, degree in indegree.items():
            if not degree:
                queue.append(ch)
        
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)

            for next in graph[ch]:
                indegree[next] -= 1
                if not indegree[next]:
                    queue.append(next)

        return ''.join(order) if len(order) == len(indegree) else ""
        

