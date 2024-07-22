import os
# Link the apps you want to open.
paths = [
  'C:\\Path\\to\\Program1',
  'C:\\Path\\to\\Program2',
  'C:\\Path\\to\\Program3', ...
]
for path in paths:
  if "Program1" in path.lower():
    # Open Program1 with specific URL
    os.system(f'start "" "{path}" "website1"')
  elif "Program2" in path.lower():
    # Open Program2 with specific URL
    os.system(f'start "" "{path}" "website1"')
    os.system(f'start "" "{path}" "website2"')
  else:
    # Otherwise, just open the path
    os.system(f'start "" "{path}"')
