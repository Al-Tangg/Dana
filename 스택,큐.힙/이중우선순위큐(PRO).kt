import java.util.*

class Solution {
    fun solution(operations: Array<String>): IntArray {
        var minHeap = PriorityQueue<Int>()
        var maxHeap = PriorityQueue<Int>(Comparator.reverseOrder())
        
        for (op in operations) {
            val (com, num) = op.split(" ")
            
            when(com) {
                "I" -> {
                    minHeap.offer(num.toInt())
                    maxHeap.offer(num.toInt())
                }
                "D" -> {
                    if (num == "1") {
                        val v = maxHeap.poll()
                        minHeap.remove(v)
                    }
                    else {
                        val v = minHeap.poll()
                        maxHeap.remove(v)
                    }
                }
            }
        }
        
        return if (minHeap.size >0) intArrayOf(maxHeap.poll(), minHeap.poll()); else intArrayOf(0, 0)
    }
}