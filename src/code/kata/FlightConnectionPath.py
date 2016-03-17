"""
Given a list of airline tickets (in some order)
[IAD -> DEN, SFO -> IAD, DEN -> ZAW, LAX -> SFO]
src: (IAD, DEN, LAX, SFO)
dst: (IAD, DEN, SFO, ZAW)



We want to put them into an iternary order (as if I'm flying from LAX to JFK)
[LAX -> SFO, SFO -> IAD, IAD -> DEN, DEN -> JFK]

Every ticket has a start and an end.
"""
# unorderedTickets = {'IAD' : 'DEN',
#                     'DEN' : 'SFO',
#                     'JFK' : 'SD',
#                     'SD' : 'LAX',...
#
#                     }
# TODO: Asked in next bit
# FIXME: fix this snippet soon
# SFO -> IAD, IAD -> DEN
def arrangeItinerary(unorderedTickets):
    if not unorderedTickets:
        return None

    # list of tuples for the ordered TIckets
    # ('IAD', 'DEN')

    sources = sorted(unorderedTickets.keys())
    destinations = sorted([v for k,v  in unorderedTickets.iterItems()])


    startPoints  = sources - destinations
    if len(startPoints) > 1:

       for startn in startPoints:
           visited = [startn]
           while(dst not in visited and unorderedTickets.containsKey(temp)):

               dst = unorderedTickets.get(temp)
               if dst not in visited:
                    visited.append(dst)

               print ('%s -> %s,' % (temp, dst))
               temp = dst

    temp = startPoints.get(0)

    if len(startPoints) == 0:
       temp = startPoints.get(0)

    visited = [temp]
    while(dst not in visited and unorderedTickets.containsKey(temp)):

       dst = unorderedTickets.get(temp)
       if dst not in visited:
           visited.append(dst)

       print ('%s -> %s,' % (temp, dst))
       temp = dst

    return temp