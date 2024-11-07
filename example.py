from astropy.coordinates import SkyCoord
from astropy import units as u

estrella1 = SkyCoord(ra=10.684*u.deg, dec=41.269*u.deg, distance=770*u.lightyear)
estrella2 = SkyCoord(ra=56.75*u.deg, dec=24.1167*u.deg, distance=600*u.lightyear)

distancia = estrella1.separation_3d(estrella2)
print(f"La distancia entre las estrellas es: {distancia.to(u.lightyear):.2f}")
