from django.db import models

CASE_CHOICES = [
    ('Ai03 Keyboards Polaris', 'Ai03 Keyboards Polaris'),
    ('Demo & Airpotter Arc80 TKL', 'Demo & Airpotter Arc80 TKL'),
    ('Dixie Mech Bauer', 'Dixie Mech Bauer'),
    ('Dixie Mech Bauer 2', 'Dixie Mech Bauer 2'),
    ('CannonKeys Brutal 60', 'CannonKeys Brutal 60'),
    ('CannonKeys Chimera 65', 'CannonKeys Chimera 65'),
    ('CannonKeys Savage 65', 'CannonKeys Savage 65'),
    ('Crykyn Dawn 75%', 'Crykyn Dawn 75%'),
    ('Exclusive E6.5', 'Exclusive E6.5'),
    ('Exclusive E7', 'Exclusive E7'),
    ('Exclusive E7-v2', 'Exclusive E7-v2'),
    ('Exclusive E8.5 TKL', 'Exclusive E8.5 TKL'),
    ('Fox Lab Time TKL', 'Fox Lab Time TKL'),
    ('Funderburker TMOv1', 'Funderburker TMOv1'),
    ('Funderburker TMOv2', 'Funderburker TMOv2'),
    ('Keycult No.1/60', 'Keycult No.1/60'),
    ('Keycult No.1/65', 'Keycult No.1/65'),
    ('Keycult No.1 TKL', 'Keycult No.1 TKL'),
    ('Keycult No.1 TKL Rev.1', 'Keycult No.1 TKL Rev. 1'),
    ('Keycult No.2/65', 'Keycult No.2/65'),
    ('Keycult No.2 TKL', 'Keycult No.2 TKL'),
    ('Keycult No.2 TKL Rev. 1', 'Keycult No.2 TKL Rev. 1'),
    ('Lin Montage', 'Lin Montage'),
    ('LZ PhysiX', 'LZ PhysiX'),
    ('Mekanisk Fjell', 'Mekanisk Fjell'),
    ('Mekanisk Klippe', 'Mekanisk Klippe'),
    ('Mekanisk Tind', 'Mekanisk Tind'),
    ('Norbauer Heavy-9', 'Norbauer Heavy-9'),
    ('Norbauer Heavy-6', 'Norbauer Heavy-6'),
    ('Norbauer Heavy Grail', 'Norbauer Grail'),
    ('Norbauer Norbaforce', 'Norbauer Norbaforce'),
    ('Norbauer Norbaforce Mark II', 'Norbauer Norbaforce Mark II'),
    ('Norbauer Novatouch', 'Norbauer Novatouch'),
    ('Noxary 268', 'Noxary 268'),
    ('Noxary 268.2', 'Noxary 268.2'),
    ('Noxary XRF', 'Noxary XRF'),
    ('OLKB Planck', 'OLKB Planck'),
    ('OLKB Preonic', 'OLKB Preonic'),
    ('Percent Studio Canoe', 'Percent Studio Canoe'),
    ('Percent Studio Canoe Gen2', 'Percent Studio Canoe Gen2'),
    ('Prime Keyboards Prime_E', 'Prime Keyboards Prime_E'),
    ('Project Keyboard Kepler', 'Project Keyboard Kepler'),
    ('Project Keyboard Kepler FC65', 'Project Keyboard Kepler FC65'),
    ('Project Keyboard Sirius', 'Project Keyboard Sirius'),
    ('Project Keyboard Tengu', 'Project Keyboard Tengu'),
    ('Proto[Typist] J-01', 'Proto[Typist] J-01'),
    ('Proto[Typist] J-02', 'Proto[Typist] J-02'),
    ('Quantic Kyuu 65%', 'Quantic Kyuu 65%'),
    ('Rama Kara', 'Rama Kara'),
    ('Rama Koyu', 'Rama Koyu'),
    ('Rama M60-A', 'Rama M60-A'),
    ('Rama M60-A SEQ2', 'Rama M60-A SEQ2'),
    ('Rama M65-A', 'Rama M65-A'),
    ('Rama M65-B', 'Rama M65-B'),
    ('Rama U80-A SEQ2', 'Rama U80-ASEQ2'),
    ('Reconsiderit Southpaw 65+', 'Reconsiderit Southpaw 65+'),
    ('Salamander TKL', 'Salamander TKL'),
    ('Satisfaction 75', 'Satisfaction 75'),
    ('Satisfaction 75 r2', 'Satisfaction 75 r2'),
    ('Smith + Rune Iron 165', 'Smith + Rune Iron 165'),
    ('Smith + Rune Iron 180', 'Smith + Rune Iron 180'),
    ('TGR 910', 'TGR 910'),
    ('TGR Alice', 'TGR Alice'),
    ('TGR Jane', 'TGR Jane'),
    ('TGR Jane v2', 'TGR Jane v2'),
    ('TGR Jane v2 CE', 'TGR Jane v2 CE'),
    ('The Key Company CandyBar Premium', 'The Key Company CandyBar Premium'),
    ('Think 6.5 v1', 'Think 6.5 v1'),
    ('Think 6.5 v2', 'Think 6.5 v2'),
    ('Wilba.Tech Thermal', 'Wilba.Tech Thermal'),
    ('Xeno', 'Xeno'),
    ('Zambumon Sar', 'Zambumon Sar'),
    ('Zambumon Verne', 'Zambumon Verne'),
    ('Other', 'Other'),
]

PCB_CHOICES = [
    ('Solderable', 'Solderable'),
    ('Hotswap', 'Hotswap'),
    ('No PCB(handwired)', 'No PCB(handwired)'),
]

PLATE_CHOICES = [
    ('Acrylic', 'Acrylic'),
    ('Acrylic Half Plate', 'Acrylic Half Plate'),
    ('Aluminum', 'Aluminum'),
    ('Aluminum Half Plate', 'Aluminum Half Plate'),
    ('Brass', 'Brass'),
    ('Brass Half Plate', 'Brass Half Plate'),
    ('Carbon Fiber', 'Carbon Fiber'),
    ('Carbon Fiber Half Plate', 'Carbon Fiber Half Plate'),
    ('Integrated', 'Integrated'),
    ('Integrated Half Plate', 'Integrated Half Plate'),
    ('Polycarbonate', 'Polycarbonate'),
    ('Polycarbonate Half Plate', 'Polycarbonate Half Plate'),
    ('POM', 'POM'),
    ('POM Half Plate', 'POM Half Plate'),
    ('Stainless Steel', 'Stainless Steel'),
    ('Stainless Steel Half Plate', 'Stainless Steel Half Plate'),
    ('Titanium', 'Titanium'),
    ('Titanium Half Plate', 'Titanium Half Plate'),
    ('Other', 'Other'),
    ('None', 'None'),
]

STABILIZER_CHOICES = [
    ('C3 Equalz Stabilizers', 'C3 Equalz Stabilizers'),
    ('Cherry Stabilizers', 'Cherry Stabilizers'),
    ('EverGlide Stabilizers', 'EverGlide Stabilizers'),
    ('Durock Stabilizers', 'Durock Stabilizers'),
    ('Zeal PC Stabilizers', 'Zeal PC Stabilizers'),
    ('Others', 'Others'),
    ('None', 'None'),
]

SWITCH_CHOICES = [
    ('C3 Tangerines', 'C3 Tangerines'),
    ('Cherry MX Black', 'Cherry MX Black'),
    ('Cherry MX Blue', 'Cherry MX Blue'),
    ('Cherry MX Brown', 'Cherry MX Brown'),
    ('Cherry MX Clear', 'Cherry MX Clear'),
    ('Cherry MX Green', 'Cherry MX Green'),
    ('Cherry MX Grey', 'Cherry MX Grey'),
    ('Cherry MX Red', 'Cherry MX Red'),
    ('Cherry MX Silent Black', 'Cherry MX Silent Black'),
    ('Cherry MX Silent Red', 'Cherry MX Silent Red'),
    ('Cherry MX Speed Silvers', 'Cherry MX Speed Silvers'),
    ('Cherry MX White', 'Cherry MX White'),
    ('Cherry MX Yellow', 'Cherry MX Yellow'),
    ('Kailh Black', 'Kailh Black'),
    ('Kailh Blue', 'Kailh Blue'),
    ('Kailh Brown', 'Kailh Brown'),
    ('Kailh Red', 'Kailh Red'),
    ('Kailh Box Navy', 'Kailh Box Navy'),
    ('Kailh Pro Burgundy', 'Kailh Pro Burgundy'),
    ('Kailh Pro Purple', 'Kailh Pro Purple'),
    ('Kailh Pro Light Green', 'Kailh Pro Light Green'),
    ('Kailh Pro Heavy Berry', 'Kailh Pro Heavy Berry'),
    ('Kailh Pro Heavy Plum', 'Kailh Pro Heavy Plum'),
    ('Kailh Pro Heavy Sage', 'Kailh Pro Heavy Sage'),
    ('Gateron Black', 'Gateron Black'),
    ('Gateron Blue', 'Gateron Blue'),
    ('Gateron Brown', 'Gateron Brown'),
    ('Gateron Clear', 'Gateron Clear'),
    ('Gateron Green', 'Gateron Green'),
    ('Gateron Inks', 'Gateron Inks'),
    ('Gateron Red', 'Gateron Red'),
    ('Gateron Yellow', 'Gateron Yellow'),
    ('Gateron Silent Black', 'Gateron Silent Black'),
    ('Gateron Silent Brown', 'Gateron Silent Brown'),
    ('Gateron Silent Clear', 'Gateron Silent Clear'),
    ('Gateron Silent Inks', 'Gateron Silent Inks'),
    ('Gateron Silent Red', 'Gateron Silent Red'),
    ('Gateron Silent Yellow', 'Gateron Silent Yellow'),
    ('Drop Holy Pandas', 'Drop Holy Pandas'),
    ('Zeal Healio', 'Zeal Healio'),
    ('Zeal Tealio', 'Zeal Tealio'),
    ('Zeal Roselio', 'Zeal Roselio'),
    ('Zeal Sakurio', 'Zeal Sakurio'),
    ('Zeal Zealio', 'Zeal Zealio'),
    ('Zeal Zilent', 'Zeal Zilent'),
    ('Others', 'Others'),
]

KEYCAP_CHOICES = [
    ('Other', 'Other'),
]


class KeyboardList(models.Model):
    username = models.CharField(max_length=80, blank=False, null=False)
    case = models.CharField(max_length=80, blank=False, choices=CASE_CHOICES)
    pcb = models.CharField(max_length=30, blank=False, choices=PCB_CHOICES)
    plate = models.CharField(max_length=50, blank=False,  choices=PLATE_CHOICES)
    stabilizers = models.CharField(max_length=30, blank=False, choices=STABILIZER_CHOICES)
    switches = models.CharField(max_length=50, blank=False, choices=SWITCH_CHOICES)
    keycaps = models.CharField(max_length=100, blank=False, choices=KEYCAP_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=300, default="", blank=True)
    email = models.EmailField(max_length=100, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}-{}".format(self.username, self.case)
