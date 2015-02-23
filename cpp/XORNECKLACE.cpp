#include <cstdio>
#include <algorithm>

using namespace std;

int n, a[500];
long long x[500];

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", a + i);

		long long m = 0;
		for (int s = 0; s < n - 1; ++s)
		{
			x[s] = 0;
			for (int c = s + 1; c < n; ++c)
			{
				x[c] = 0;
				for (int o = s; o < c; ++o)
					x[c] = max(x[c], x[o] + (a[c] ^ a[o]));

				m = max(m, x[c] + (a[c] ^ a[s]));
			}
		}

		printf("%lld\n", m);
	}
	
	return 0;
}