import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var q: Queue<Int> = LinkedList()
        
        for (i in 0 until bridge_length - 1) {
            q.offer(0)
        }
        q.offer(truck_weights[0])
        
        var t = 1
        var i = 1
        
        while (q.sum() > 0) {
            q.poll()
            
            if (i < truck_weights.size && q.sum() + truck_weights[i] <= weight) {
                q.offer(truck_weights[i])
                i += 1
            } else {
                q.offer(0)
            }
            t += 1
        }
        
        return t
    }
}