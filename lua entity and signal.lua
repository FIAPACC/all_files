local Signal = {}
Signal.__index = Signal

local Connection = {}
Connection.__index = Connection

function Connection.new(callback)
  return setmetatable({
    _callback = callback,
    connected = true,
  }, Connection)
end

function Connection:Disconnect()
  setmetatable(self, nil)
  self = nil
end

function Signal.new()
  return setmetatable({Connections = {}}, Signal)
end

function Signal:Fire(...)
  local ok = true
  for _, con in pairs(self.Connections) do
    local result = pcall(con._callback,...)
    if not result then ok = false end
  end
  return ok
end

function Signal:Connect(callback)
  assert(type(callback) == 'function', 'callback must be function')
  
  local con = Connection.new(callback)
  table.insert(self.Connections, con)

  return con
end

function Signal:Once(callback)
  assert(type(callback) == 'function', 'callback must be function')
  
  local con
  con = self:Connect(function(...)
    con:Disconnect()
    callback(...)
  end)
  return con
end

--------------------------

local entity = {}
entity.__index = entity

--[[type entityType = {
  name : string ?,
  damage : number ?,
  health : number ?
}]]

--export type entityCLassType = typeof(setmetatable({}, entity))

function entity.new(entityTab --[[: entityType]]) --: entityCLassType
  local self = setmetatable({}, entity)
  self.name = entityTab.name or "Default"
  self.damage = entityTab.damage or 8
  self.health = entityTab.health or 100

  self:_init()
   
  print('Entity '..self.name..' was created.')
  return self --:: entityCLassType
end

function entity:_init()
  self.onDamageChanged = Signal.new()
  self.onHealthChanged = Signal.new()
  self.onDying = Signal.new()
  self.onDied = Signal.new()

  self.onDamageChanged:Connect(function(oldDamage)
    print('['..'Entity '..self.name..'] - [DAMAGE] : ' .. 'Went from '.. oldDamage..' to '.. self.damage..'.')
  end)

  self.onHealthChanged:Connect(function(oldHealth)
    print('['..'Entity '..self.name..'] - [HEALTH] : '.. 'Went from '.. oldHealth..' to '.. self.health..'.')
  end)

  self.onDying:Connect(function()
    print('['..'Entity '..self.name..'] - [DYING]')
  end)

  self.onDied:Connect(function()
    print('['..'Entity '..self.name..'] - [DIED]')
  end)

  self._init = nil
  return self
end

function entity:Destroy()
  for i, k in self do 
   self[i] = nil
  end
  self = nil

  return self
end

function entity:Die()
  self.onDying:Fire(self.health)

  self.health = 0

  self.onDied:Fire()
  return self
end

function entity:TakeDamage(amount)
  local oldHealth = self.health
  amount = amount > self.health and self.health or amount
  self.health = self.health - amount
  self.onHealthChanged:Fire(oldHealth)
  if self.health <= 0 then self:Die() end

  return self
end

function entity:Attack(target --[[: entityCLassType]])
  if not target or self.health <= 0 then return end
  target:TakeDamage(self.damage)

  return self
end

local default1 = {name = 'a', damage = 10}
local default2 = {name = 'b', damage = 10}

local entity1 = entity.new(default1)
local entity2 = entity.new(default2)

entity2.onHealthChanged:Connect(function(oldHealth)
  print'linear'   
end)

entity2.onHealthChanged:Once(function(oldHealth)
  print'once'   
end)
