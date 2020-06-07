import score
import utils

class ZHeap:
    def __init__(self, item=[], id=[]):
        self.items = item
        self.ids = id
        self.heapsize = len(self.items)

    def LEFT(self, i):
        return 2 * i + 1

    def RIGHT(self, i):
        return 2 * i + 2

    def PARENT(self, i):
        return int((i - 1) / 2)

    def MIN_HEAPIFY(self, i):
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.heapsize and self.items[l] < self.items[i]:
            smallest = l
        else:
            smallest = i

        if r < self.heapsize and self.items[r] < self.items[smallest]:
            smallest = r

        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.ids[i], self.ids[smallest] = self.ids[smallest], self.ids[i]
            self.MIN_HEAPIFY(smallest)

    def INSERT(self, val,id):
        self.items.append(val)
        self.ids.append(id)
        idx = len(self.items) - 1
        parIdx = int(self.PARENT(idx))
        while parIdx >= 0:
            if self.items[parIdx] > self.items[idx]:
                self.items[parIdx], self.items[idx] = self.items[idx], self.items[parIdx]
                self.ids[parIdx], self.ids[idx] = self.ids[idx], self.ids[parIdx]
                idx = parIdx
                parIdx = self.PARENT(parIdx)
            else:
                break
        self.heapsize += 1

    def DELETE(self):
        last = len(self.items) - 1
        if last < 0:
            return None
        # else:
        self.items[0], self.items[last] = self.items[last], self.items[0]
        self.ids[0], self.ids[last] = self.ids[last], self.ids[0]
        val = self.items.pop()
        id = self.ids.pop()
        self.heapsize -= 1
        self.MIN_HEAPIFY(0)
        return id


    def BUILD_MIN_HEAP(self):
        i = self.PARENT(len(self.items) - 1)
        while i >= 0:
            self.MIN_HEAPIFY(i)
            i -= 1

    def SHOW(self):
        print(self.items)


class ZPriorityQ(ZHeap):
    def __init__(self, item=[]):
        ZHeap.__init__(self, item)

    def enQ(self, val, id):
        ZHeap.INSERT(self, val, id)

    def deQ(self):
        val = ZHeap.DELETE(self)
        return val

def topK(wordlist, docID):

    K = int(input("how many doc do you want to see at most?\nprint -1 for all docs.\n"))
    print("\n\n************* Show Result ************\n\nFind ",len(docID), " docs.\n")
    #print("here is topK")
    VSM_sum = utils.get_from_file('VSM_sum')
    pq = ZPriorityQ()
    if len(docID) < K or K == -1:
        K = len(docID)
    for doc in docID:
        doc_score = VSM_sum[str(doc)]
        pq.enQ(doc_score, doc)
    result = []
    for i in range(K):
        doc = pq.deQ()
        #print(doc)
        result.append(doc)
    print("Show ", len(result), " docs.\n")
    print(result)
    stop = input("\nPress any key to show articles...\n")
    return result