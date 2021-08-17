import json
import sys
from docassemble.base.util import path_and_mimetype, log
from typing import Union

__all__ = ['poverty_scale_income_qualifies',
           'get_poverty_scale_data',
          ]

ps_poverty_scale_json_path = path_and_mimetype("data/sources/federal_poverty_scale.json")[0]

ps_data = {}
try:
  with open(ps_poverty_scale_json_path) as f:
    ps_data = json.load(f)
except FileNotFoundError:
  log(f"Cannot determine poverty scale: unable to locate file {ps_poverty_scale_json_path}")
except JSONDecodeError as e:
  log(f"Cannot determine poverty scale: is {ps_poverty_scale_json_path} a valid JSON file? Error was {e}")


def get_poverty_scale_data():
  return ps_data
  

def poverty_scale_income_qualifies(total_monthly_income:float, household_size:int=1, multiplier:int=1)->Union[bool,None]:
  """
  Given monthly income, household size, and an optional multiplier, return whether an individual
  is at or below the federal poverty level.
  
  Returns None if the poverty level data JSON could not be loaded.
  """
  # Globals: poverty_increment and poverty_base
  if not ps_data:
    return None
  additional_income_allowed = household_size * poverty_increment
  household_income_limit = (poverty_base + additional_income_allowed) * multiplier
  return int((household_income_limit)/12) >=  int(total_monthly_income)
