# import simplekml
# from polycircles import polycircles
#
# kml = simplekml.Kml()
# out_boundaries = polycircles.circle(31.830039, 35.071011, 100, 72)
# in_boundaries = polycircles.circle(31.830039, 35.071011, 90, 72)
# out_boundaries = [t[::-1] for t in out_boundaries]
# in_boundaries = [t[::-1] for t in in_boundaries]
#
# pol = kml.newpolygon(name="Nataf entrance",
#                      outerboundaryis=out_boundaries,
#                      innerboundaryis=in_boundaries)
# pol.style.polystyle.color = simplekml.Color.green
# print(pol)
# kml.save("/tmp/nat2.kml")
#
