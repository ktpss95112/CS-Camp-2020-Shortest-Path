#include <bits/stdc++.h>
using namespace std;

typedef int ll; // you can change to long long (?)
const int N = 808; // number of vertex
const int M = 888; // number of edges
const int INF = 0x3f3f3f3f;

int n = 0, m = 0;
ll dp[N][N];
ll par[N][N];
map<string, ll> mp;
string rev_mp[N];
ll u[M], v[M], w[M];

void init() {
    memset(dp, INF, sizeof(dp));
    memset(par, -1, sizeof(par));
    for (int i = 0; i < N; ++i) {
        dp[i][i] = 0;
    }
}

int get_node_id(string s) {
    if (mp.find(s) != mp.end()) {
        return mp[s];
    }
    else {
        mp[s] = (++n);
        rev_mp[n] = s;
        return mp[s];
    }
}

void read_input(char* file) {
    fstream fs;
    fs.open(file, ios::in);
    string s;
    while (getline(fs, s)) {
        ++m;
        stringstream ss;
        ss.str(s);
        string s1, s2, s3;
        ll s4;
        ss >> s1 >> s2 >> s3 >> s4;
        // cerr << "s1 = " << s1 << " , s2 = " << s2 << " , s3 = " << s3 << " , s4 = " << s4 << endl;
        u[m] = get_node_id(s1);
        v[m] = get_node_id(s2);
        w[m] = s4;
    }
    cerr << "finish reading input, m = " << m << " , n = " << n << endl;
    /* for (int i = 1; i <= m; ++i) {
        cerr << u[i] << ' ' << v[i] << ' ' << w[i] << endl;
    } */
}

void U(int i, int j, ll _par, ll val1, ll val2) {
    ll val = val1 + val2;
    if (val < dp[i][j]) {
        dp[i][j] = val;
        par[i][j] = _par;
    }
}

void cal_dp() {
    for (int i = 1; i <= m; ++i) {
        U(u[i], v[i], u[i], w[i], 0);
        U(v[i], u[i], v[i], w[i], 0);
    }
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                U(i, j, k, dp[i][k], dp[k][j]);
            }
        }
    }
}

vector<int> path;

void find_path(int u, int v) {
    if (par[u][v] == u) {
        path.push_back(u);
        return;
    }
    find_path(u, par[u][v]);
    find_path(par[u][v], v);
}

void query(int u, int v) {
    cout << "shortest path weight = " << dp[u][v] << endl;
    path.clear();
    find_path(u, v);
    path.push_back(v);
    for (int i: path) cout << rev_mp[i] << ' ';
    cout << endl;
}

void query_2(int st, int nn, vector<int> per) {
    sort(per.begin(), per.end());
    vector<int> best;
    int ans = INF;
    do {
        int tmp = dp[st][ per[0] ];
        for (int i = 1; i < nn; ++i) {
            tmp += dp[ per[i - 1] ][ per[i] ];
        }
        if (tmp < ans) {
            ans = tmp;
            best = per;
        }
    } while (next_permutation(per.begin(), per.end()));
    cout << "best TSP weight = " << ans << endl;
    cout << rev_mp[st] << ' ';
    for (int i: best) cout << rev_mp[i] << ' ';
    cout << endl;
}

int main (int argc, char** argv) {
    if (argc != 2) {
        cerr << "Usage: ./a.out [input_file]" << endl;
        return 0;
    }
    cerr << "welcome to this program" << endl;
    cerr << "all the error message will show on stderr, and the output of query will show on stdout, notice that the algorithm is O(n!) instead of O(n^2 2^n)" << endl;
    init();
    read_input(argv[1]);
    cal_dp();
    cerr << "query スタート" << endl;
    cerr << "input {[start-vertex] [len of permutation] [permutation] to query" << endl;
    cerr << "for example: " << endl;
    cerr << "H 8 C E I F L N R Q" << endl;
    cerr << endl << "input EOF as terminate of query" << endl;
    string u, v;
    while (cin >> u) {
        bool flag = false;
        if (mp.find(u) == mp.end()) {
            cerr << "vertex " << u << " does not exist" << endl;
            flag = true;
        }
        int n; cin >> n;
        vector<int> vs;
        for (int i = 0; i < n; ++i) {
            string tmp; cin >> tmp;
            if (mp.find(tmp) == mp.end()) {
                cerr << "vertex " << tmp << " does not exist" << endl;
                exit(0);
            }
            vs.push_back(get_node_id(tmp));
        }
        query_2(get_node_id(u), n, vs);
    }
}

