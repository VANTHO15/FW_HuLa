#include "Gpio_TS_001.h"

#define LENGTH 10

uint8_t Id;
uint8_t TestCaseResult[LENGTH];

void RESULT_RunAllTests(RESULT_TestSuite_t* TS)
{
    for(Id = 0; Id < LENGTH; Id++)
    {
        TestCaseResult[Id] = 2;   // ban dầu là Not Run
    }
    for(Id = 0; Id < TS->TC_Count; Id++)
    {
        TestCaseResult[Id] = 0;   // set false
        TS->TC_Ptr[Id]();
    }
    __asm volatile(".globl ThoNVEnd");
    __asm volatile("ThoNVEnd:");
    __asm volatile("CMP R1,#1");
}

void RESULT_Assert(uint8_t result)
{
    if(result)
    {
        /*  Test True */
        TestCaseResult[Id] = 1;
    }
}
RESULT_TestCase_t Array_TC_OF_TS[]= {Gpio_TC_001,Gpio_TC_002};
RESULT_TestSuite_t THONV_TS_STRUCT= { sizeof(Array_TC_OF_TS)/sizeof(Array_TC_OF_TS[0]) , Array_TC_OF_TS };

int main(void) 
{
    RESULT_RunAllTests(&THONV_TS_STRUCT);
}