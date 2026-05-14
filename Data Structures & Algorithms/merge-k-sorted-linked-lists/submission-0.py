# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        for k, node in enumerate(lists):
            minHeap.append([k, node.val, node])

        size = len(minHeap)

        def heapify(minHeap, size, i):
            smallest = i
            left = 2 * smallest + 1
            right = 2 * smallest + 2

            if left < size and minHeap[left][1] < minHeap[smallest][1]:
                smallest = left

            if right < size and minHeap[right][1] < minHeap[smallest][1]:
                smallest = right

            if smallest != i:
                minHeap[smallest], minHeap[i] = minHeap[i], minHeap[smallest]
                heapify(minHeap, size, smallest)                  
        
        def buildMinHeap(minHeap, size):
            for i in range((size - 1) // 2, -1, -1):
                heapify(minHeap, size, i)

        buildMinHeap(minHeap, size)
        dummy = current = ListNode()

        while size > 0:
            list_index, value, node = minHeap[0]
            current.next = node
            current = current.next

            if node.next:
                # Replace with next node from same list
                minHeap[0] = [list_index, node.next.val, node.next]
            else:
                # Finish one list in lists, decrease size
                minHeap[0] = minHeap[size - 1]
                minHeap.pop()
                size -= 1
            
            heapify(minHeap, size, 0)
        return dummy.next