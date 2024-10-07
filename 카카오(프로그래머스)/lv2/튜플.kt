class Solution {
    fun solution(s: String): IntArray {
        var answer = mutableListOf<Int>()
        
        
        val sArr = s.replace("{{","").replace("}}","").split("},{")
        val sortedArr = sArr.sortedBy{ it.length }
        
        for (s in sortedArr) {
            val sList = s.split(",").map{it.toInt()}
            for (i in sList) {
                if (i !in answer) {
                    answer.add(i)
                }
            }
        }
        
        return answer.toIntArray()
    }
}