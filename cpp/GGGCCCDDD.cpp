#include <cstdio>
#include <vector>

using namespace std;

const int R = 1000000007;

int n;

int gcd(int a, int b) { return a ? gcd(b%a, a) : b; }
int g[1001][1001];

using vi = vector<int>;

vi d;

vi prod(vi a, vi b)
{
	vi ret = vi(n + 1);
	for (int i = 1; i < n + 1; ++i)
	{
		for (int j = 1; j < n + 1; ++j)
		{
			int v = g[i][j];
			ret[v] = (ret[v] + (int)((long long)a[i] * b[j] % R)) % R;
		}
	}

	return ret;
}

vi go(int e)
{
	vi ret;
	if (e == 1)
		ret = d;
	else
	{
		vi h = go(e / 2);
		ret = prod(h, h);
		if (e % 2)
			ret = prod(ret, d);
	}

	return ret;
}

int main()
{
	for (int i = 0; i < 1001; ++i)
	for (int j = 0; j < 1001; ++j)
		g[i][j] = gcd(i, j);
	
	int t;
	scanf("%d", &t);
	while (t--)
	{
		int m;
		scanf("%d %d", &n, &m);
		d = vi(n + 1, 1);
		d[0] = 0;
		
		vi c = go(m);
		long long s = 0;
		for (long long i = 1; i < n + 1; ++i)
		{
			s += c[i] * i;
			s %= R;
		}

		printf("%d\n", s);
	}
	
	return 0;
}