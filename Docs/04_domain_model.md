# domain concepts

| requirment | huomiot|  
|:-----|:---:|  
| Tuote pitää saada sammutettua <br> manuaalisesti ja automaattisesti. | sammutus, <br> manuaalisesti, <br> automaatio |  
| Tuoteen kuntoa/tilaa voidaan <br>valvoa tietokoneelta. | tuotteen valvonta |
| Valoja voidaan ohjelmoida <br> sammumaan tai  käynnistymään <br> tiettyyn kellon aikaan. | valo,<br> sammutus,<br> käynnistys |  
| Valon määrää on <br> säädettävä/muokattava. | säädettävä valo |

## domain model

**Virta**  
- On/off per valo Bool

**Valo**  
- Intensity/kirkkaus int
- State/tila otetaan virrasta bool 
- location/sijainti string/int

**COMController**
- Yhdistetty valoihin hallintaa varten.
- Näyttää valojen sijainnit/huoneet. string/int
- Näyttää valojen state/tila. bool
- Näyttää valojen intensity/kirkkaus. int

**Asiakas_käyttäjä**
- voi hallita oman honeen valojen virtaa eli onko on vai off
- voi hallita valojen kirkkautta fyysisesti kytkimestä

**Tuoteen_Omistaja/ADMIN**
- Hallinta COMController interface.