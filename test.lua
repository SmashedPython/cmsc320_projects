----------------------------------------------------------------------
-- Macbeth region ipelet
----------------------------------------------------------------------

label = "Macbeth Region"

-- Ensure revertOriginal is properly defined
revertOriginal = revertOriginal or function() end

about = [[
Generate a Macbeth region for a polygon, best used with shortcuts.

This Lua ipelet script is written by Hongyang Du hongyangdu182@gmail.com.
]]

shortcuts.ipelet_macbeth_region = "Ctrl+M"  -- Assigning a shortcut (Ctrl+M) for the ipelet

require("ipe")

function run(model,num)
  -- Check if we have something selected
  local p = model:page()
  if not p:hasSelection() then
    model.ui:explain("No selection")
    return
  end

  -- Check if both a polygon and a point are found
  local selectedObjects = model:page():selectedObjects()
  if not selectedObjects or #selectedObjects ~= 2 then
    model.ui:explain("Please select one polygon and one point inside the polygon.")
    return
  end

  -- Store the polygonVertices and the point coordinate
  local polygonVertices = {}
  local pointCoordinates = {}

  -- Iterate through the selected objects to identify the polygon and point
  for _, obj in ipairs(selectedObjects) do
    if obj:type() == "shape" then
      local shape = obj:shape()
      if shape:isPolygon() then
        local path = shape:path()
        for j = 1, path:size() - 1 do
          table.insert(polygonVertices, {path:at(j):x(), path:at(j):y()})
        end
      elseif shape:isMark() and shape:text() == "point" then
        pointCoordinates = {shape:pos():x(), shape:pos():y()}
      end
    end
  end

  if #polygonVertices == 0 or #pointCoordinates == 0 then
    model.ui:explain("Please select one polygon and one point inside the polygon.")
    return
  end

  -- Create a new path for the polygon based on the subtraction of coordinates
  local newPath = ipe.Path(#polygonVertices + 1)  -- +1 for closing the polygon
  for _, vertex in ipairs(polygonVertices) do
    local newX = pointCoordinates[1] - vertex[1]
    local newY = pointCoordinates[2] - vertex[2]
    newPath:append(newX, newY)
  end

  -- Close the new polygon by adding the first vertex
  local firstVertex = polygonVertices[1]
  local firstNewX = pointCoordinates[1] - firstVertex[1]
  local firstNewY = pointCoordinates[2] - firstVertex[2]
  newPath:append(firstNewX, firstNewY)

  -- Create a new shape for the new polygon
  local newPolygonShape = ipe.PathShape(newPath)
  newPolygonShape:setPen(ipe.Pen(ipe.rgb(0, 0, 0), "black"))
  newPolygonShape:setBrush(ipe.Brush())

  -- Add the new polygon object to the current page
  model:beginMacro("Create New Polygon")
  model:insert(newPolygonShape)
  model:endMacro()

  model.ui:explain("New polygon created successfully")
end
