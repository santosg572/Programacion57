#include <iostream>
using namespace std;

const int maxCard = 16;
enum Bool { False, True };
enum ErrCode { noErr, overflow };

class Set {
   int elems[maxCard];
   int card;
public:
   void EmptySet () { card = 0; }
   Bool Member (int );
};

Bool Set::Member (int elem)
{
   for (int i=0; i < card; ++i)
      if (elems[i] == elem)
         return True;
   return False;
}


int main()
{
   Set s1, s2, s3;
}

