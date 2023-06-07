#include <algorithm>
#include <iostream>

using namespace std;

int main() 
{
	int person[9] = { 0 };
	int sum = 0;

	for (int i = 0; i < 9; i++)
	{
		cin >> person[i];
		sum += person[i];
	}

	sort(person, person + 9);

	int remain = sum - 100;
	for (int i = 0; i < 8; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if (remain == (person[i] + person[j]))
			{
				for (int k = 0; k < 9; k++)
				{
					if (k != i && k != j)
					{
						cout << person[k] << "\n";
					}
				}
				return 0;
			}
		}
	}

	return 0;
}

