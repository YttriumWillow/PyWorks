import json
# f1 = open("temp.txt", "r", encoding = "utf-8")
l = json.loads("  \"advancements.adventure.adventuring_time.title\": \"Adventuring Time\",\
  \"advancements.adventure.adventuring_time.description\": \"Discover every biome\",\
  \"advancements.adventure.arbalistic.title\": \"Arbalistic\",\
  \"advancements.adventure.arbalistic.description\": \"Kill five unique mobs with one crossbow shot\",\
  \"advancements.adventure.bullseye.title\": \"Bullseye\",\
  \"advancements.adventure.bullseye.description\": \"Hit the bullseye of a Target block from at least 30 meters away\",\
  \"advancements.adventure.walk_on_powder_snow_with_leather_boots.title\": \"Light as a Rabbit\",\
  \"advancements.adventure.walk_on_powder_snow_with_leather_boots.description\": \"Walk on powder snow...without sinking in it\",\
  \"advancements.adventure.lightning_rod_with_villager_no_fire.title\": \"Surge Protector\",\
  \"advancements.adventure.lightning_rod_with_villager_no_fire.description\": \"Protect a villager from an undesired shock without starting a fire\",\
  \"advancements.adventure.spyglass_at_parrot.title\": \"Is It a Bird?\",\
  \"advancements.adventure.spyglass_at_parrot.description\": \"Look at a parrot through a spyglass\",\
  \"advancements.adventure.spyglass_at_ghast.title\": \"Is It a Balloon?\",")
print(l.keys)