"""
AI's will handle any automated action for an object.
It must support a scripted behavior passed from something else, like mapgen.
It must be affected by scenarios, like a village being attacked.
This impacts the local level only,
it will defer control to groups when abstract.

The AI component will handle the glue between the various objects
Long Term State and Short Term state will only keep track of events.
The Personality of an AI will decide what Behaviors to call based on its
environment and states.
Example, most happy goblins will cheerfully kill any possible victims while
a happy bear could be more inclined to avoid confrontations.

Personalities should however defer to the given Scripted behavior when needed.
A sudden invasion would certainly force every one to reevaluated their routine.
Plus it allows quests to have puppets to use.
"""
