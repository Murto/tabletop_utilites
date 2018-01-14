function ability_roll()
  local total = -6
  local min = 6
  for i = 1, 4 do
    local roll = math.random(1, 6)
    if (roll < min) then
      total = total + min
      min = roll
    else
      total = total + roll
    end
  end
  return total
end

math.randomseed(os.time())
local scores = {}
for i = 1, 6 do
  table.insert(scores, ability_roll())
end
print(table.concat(scores, ' '))
