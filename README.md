# fightme
something something fleet customizer and total warfare simulator

Sometime in the future this is going to get embedded within sandcastle

## TODO
- `describe_ship.py`
    - Describes ships using YAML
    - Reads from a database of ships also using YAML
    - Lets the user pick ship parts
        - Some form of parts randomization/optimization
- `engage_ships.py`
    - Reads fleets using YAML
    - Fights those fleets
        - Simulation comes once the renderer is up and we have a game loop

## Ship Representation
We want:
- Backwards compatitability
- Emphasis on fluff
- Emphasis on renderable attributes
    - Like position of turret hardpoints and angles of fire
- Able to handle simulation/non-simulation combat resolution mechanics
- Shift towards procedural generation of names

Let's try writing some yaml
```
-
    name: Brisigox Turbine Reactor
    type: Reactor
    maker: Martin Imperial
    model: XX4A-I
    specs:
        acceleration: 100
        thrust: 100
        weight: 24t
    condition: terrible
    requires: 
        - Haylor fuel
    notes: |
        Shit's expensive, and not that good
```
