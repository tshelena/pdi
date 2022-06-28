#include <bits/stdc++.h> 
using namespace std; 
 
void sub_mat_even(int N) 
{ 
  
  
  int K = 1; 
   
  
  
  int A[N][N]; 
   
  for(int i = 0; i < N; i++)
  {
    for(int j = 0; j < N; j++)
    {
      A[i][j] = K;
      K++;
    }
  }
 
  
  
  
  
  if(N % 2 == 0)
  {
    for(int i = 0; i < N; i++)
    {
      if(i % 2 == 1)
      {
        int s = 0; 
        int l = N - 1;
       
        while(s < l) 
        {
          swap(A[i][s], 
               A[i][l]);
          s++;
          l--;
        }
      }
    }
  }
 
  
  for(int i = 0; i < N; i++)
  {
    for(int j = 0; j < N; j++)
    {
      cout << A[i][j] << " ";
    }
    cout << endl;
  }
} 
 
int main() 
{ 
    int N = 4;
   
    
    sub_mat_even(N); 
} 
 