#include <algorithm>
#include <iostream>

using namespace std;


int main() 
{
	int card[20] = { 0 };
	int length = sizeof(card) / sizeof(card[0]);
	for (int i = 0; i < length; i++)
	{
		card[i] = (i + 1);
	}

	int st, ed;
	int count = 10;
	while (count != 0)
	{
		cin >> st >> ed;
		
		int len = ed - st + 1;
		int calc = 1;
		for (int i = st-1; i < ((st-1)+ int(len/2)); i++)
		{
			int temp = card[i];
			card[i] = card[i + len - calc];
			card[i + len - calc] = temp;
			calc+=2;
		}

		count--;
	}
	for (int i = 0; i < length; i++)
	{
		cout << card[i] << " ";
	}
	cout << "\n";
	
	return 0;
}

