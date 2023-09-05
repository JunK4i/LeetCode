class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        cited_at_least = 1000
        published = 0
        result = 0
        for i in range(len(citations)):
            published = i+1
            if citations[i] < cited_at_least:
                cited_at_least = citations[i]
            result = max(result, min(published, citations[i]))
        return result