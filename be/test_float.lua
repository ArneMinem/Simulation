function sysCall_init()
   sphere=sim.getObjectHandle('Sphere')
   fbuoy_nom = 4 -- 3.25
end

function sysCall_actuation()
    -- put your actuation code here
    --
    -- For example:
    --
    -- local position=sim.getObjectPosition(handle,-1)
    -- position[1]=position[1]+0.001
   -- sim.setObjectPosition(handle,-1,position)
   local position=sim.getObjectPosition(sphere, -1)
   
   local force = {0,0,0}
   local torque = {0,0,0}
   dz = position[3]
   if dz < -0.25 then
      fbuoy = fbuoy_nom
   else
      if dz < 0 then
	 fbuoy = fbuoy_nom * (-dz/0.25)
      else
	 fbuoy = 0
      end
   end
   --print (fbuoy,dz)
   force[3] = fbuoy
   sim.addForceAndTorque(sphere,force,torque)
end

function sysCall_sensing()
    -- put your sensing code here
end

function sysCall_cleanup()
    -- do some clean-up here
end

-- You can define additional system calls here:
--[[
function sysCall_suspend()
end

function sysCall_resume()
end

function sysCall_dynCallback(inData)
end

function sysCall_jointCallback(inData)
    return outData
end

function sysCall_contactCallback(inData)
    return outData
end

function sysCall_beforeCopy(inData)
    for key,value in pairs(inData.objectHandles) do
        print("Object with handle "..key.." will be copied")
    end
end

function sysCall_afterCopy(inData)
    for key,value in pairs(inData.objectHandles) do
        print("Object with handle "..key.." was copied")
    end
end

function sysCall_beforeDelete(inData)
    for key,value in pairs(inData.objectHandles) do
        print("Object with handle "..key.." will be deleted")
    end
    -- inData.allObjects indicates if all objects in the scene will be deleted
end

function sysCall_afterDelete(inData)
    for key,value in pairs(inData.objectHandles) do
        print("Object with handle "..key.." was deleted")
    end
    -- inData.allObjects indicates if all objects in the scene were deleted
end
--]]
