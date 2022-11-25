#include <iostream>
#include <math.h>
#include <map>
#include <set>
#include <queue>

using namespace std;

const int INF = 1000000000;

int main() {
    while (true) {

        int n, m, q, s;
        cin >> n >> m >> q >> s;

        if (n == 0 && m == 0 && q == 0 && s == 0) {
            return 0;
        }

        int dp[n];
        bool visited[n];
        for (int i = 0; i < n; i++) dp[i] = INF;
        for (int i = 0; i < n; i++) visited[i] = false;
        dp[s] = 0;

        int edges[n][n];
        auto edgs = vector<vector<int> >(n, vector<int>(n, 0));
        vector<int> key[n];

        for (int i = 0; i < m; i++) {
            int a, b, w;
            cin >> a >> b >> w;
            if (edgs[a][b] == 0) {
                edges[a][b] = w;
                edgs[a][b] = 1;
                key[a].push_back(b);
            }
            else {
                edges[a][b] = min(edges[a][b], w);
            }

        }

        priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;


        int curr = s;
        bool run = true;
        while (run) {
            visited[curr] = true;

            for (int neighbour : key[curr]) {
                dp[neighbour] = min(dp[neighbour], dp[curr] + edges[curr][neighbour]);
                pq.push(make_pair(dp[neighbour], neighbour));
            }

            try {
                while (visited[curr]) {
                    if (pq.size() == 0) {
                        run = false;
                        break;
                    }
                    curr = pq.top().second;
                    pq.pop();
                }   
            }
            catch (exception e) {
                break;
            }
            
        }

        for (int i = 0; i < q; i++) {
            int e;
            cin >> e;
            int val = dp[e];
            if (val == INF) {
                cout << "Impossible" << endl;
            } else {
                cout << val << endl;
            }
        }
    }

    return 0;
}