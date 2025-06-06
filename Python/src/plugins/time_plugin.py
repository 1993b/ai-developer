from typing import TypedDict, Annotated, Optional  
import requests  
import asyncio  
from semantic_kernel.functions import kernel_function
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(override=True)

class TimePlugin:  
    @kernel_function(description="Gets the current time.")
    async def get_current_time(self):
        current_time = datetime.now()
        return current_time
    
    @kernel_function(description="Get year")
    async def get_year(self, user_date):
        current_year = user_date.year
        return current_year
    
    @kernel_function(description="Get month")
    async def get_month(self, user_date):
        current_month = user_date.month
        return current_month
    
    @kernel_function(description="Get day of week")
    async def get_day_of_week(self, user_date):
        day_of_week = user_date.strftime("%A")
        return day_of_week