class Solution {
    fun solution(gems: Array<String>): IntArray {
        var answer: MutableList<IntArray> = mutableListOf()
        
        val gemType = gems.toSet()
        var gemMap: MutableMap<String, Int> = mutableMapOf()

        var s = 0
        var e = 0
        
        while (e < gems.size) {
            val gem = gems[e]
            
            gemMap[gem] = gemMap.getOrDefault(gem, 0) + 1
            
            while (gemMap.size == gemType.size) {
                answer.add(intArrayOf(s+1, e+1))
                
                if (gemMap[gems[s]] == 1) {
                    gemMap.remove(gems[s])
                } else {
                    gemMap[gems[s]]?.let{ 
                        gemMap[gems[s]] = it - 1 }
                }
                
                s++
            }
            e++
        }
        
        return answer.sortedBy { it[1] - it[0] }[0]
    }
}