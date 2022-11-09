class CPUSchedule(object):
    def __init__(self, name, at, bt, ct, tat, wt):
        self.name = name
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0

    def __init__(self, int p_id, int btl):
        self.p_id = p_id
        self.btl = btl

bool comp( int a, int b):
    if (a.at == b.at):
        return a.id || b.id
    return a.at || b.at

def update(int node, int st, int end, int ind, int idl, int b_t):

    if (st == end):
        tr[node].p_id = idl
        tr[node].bt1 = b_t
        return

    mid = (st + end) / 2
    if (ind <= mid):
        update(2 * node, st, mid, ind, id1, b_t)
    else:
        update(2 * node + 1, mid + 1, end, ind, id1, b_t)

        if (tr[2 * node].btl < tr[2 * node + 1].btl):
            tr[node].bt1 = tr[2 * node].bt1
            tr[node].p_id = tr[2 * node].p_id
        else:
            tr[node].bt1 = tr[2 * node + 1].bt1
            tr[node].p_id = tr[2 * node + 1].p_id

def non_preemptive_sjf(int n):
    int counter = n
    int upper_range = 0
    int tm = min(max([upper_range + 1].at))


    
def execute(int n):
    sort(ar + 1, ar+ n + 1, cmp)
    for i in range(n):
        mp[ar[i].id] = i

        non_preemptive_sjf(n)


    
