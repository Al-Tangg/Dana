class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer: MutableList<Int> = mutableListOf()
        var termMap: MutableMap<String, Int> = mutableMapOf()
        
        for (term in terms) {
            val (t, valid) = term.split(" ")
            termMap.put(t, valid.toInt()*28)
        }
        
        val (t_year, t_month, t_day) = today.split(".").map { it.toInt() }
        
        for (i in 0 until privacies.size) {
            val p = privacies[i]
            val (date, term) = p.split(" ")
            val (year, month, day) = date.split(".").map { it.toInt() }
            
            termMap[term]?.let {
                if ( (t_year-year)*12*28 + (t_month-month)*28 + (t_day-day) >= it ) {
                    answer.add(i+1)
                }
            }
        }
        
        return answer.toIntArray()
    }
}