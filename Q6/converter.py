import numpy as np

h = 6.67 * (10**(-27))
c = 3. * (10**(10))

#I define these constants up here in CGS units. The rest of these functions should 
#be fairly self-explanitory in their names. The biggest note is that I input my
#wavelengths in angstroms, so I code in on-the-fly conversions to-and-from angstroms

def wave_to_freq(lam):
    nu = c / (lam * (10**(-8)))
    return nu

def freq_to_wave(nu):
    lam = c / nu
    return (lam * (10**(8)))

def wave_to_nrg(lam):
    nrg = (h * c) / (lam * (10**(-8)))
    return nrg

def freq_to_nrg(nu):
    nrg = h * nu
    return nrg

def nrg_to_wave(nrg):
    lam = (h * c) / nrg
    return (lam * (10**(8)))

def nrg_to_freq(nrg):
    nu = nrg / h
    return nu

def flam_to_fnu(flam, lam):
    fnu = (flam * ((lam * (10**(-8)))**2)) / c
    return fnu

def fnu_to_flam(fnu, nu):
    flam = (fnu * (nu**2)) / c
    return flam
print "Answers given in CGS units. Input wavelengths as Angstroms"

print "5500 Angstroms in Hz : " + str(wave_to_freq(5500.))
print "5500 Angstroms in Ergs : " + str(wave_to_nrg(5500.))

#The following are conversions between F_nu and F_lam. I use a sample flux of 
#10000, then divide it out to find my exact conversion factor. I do this for 
#both F_nu and F_lam conversions. Then, I just repeat the process three times 
#for each wavelength. 

conv = wave_to_freq(3000.)

test1 = flam_to_fnu(10000., 3000.)
result1 = test1 / 10000.
test2 = fnu_to_flam(test1, conv)
result2 = test2 / test1

print "Conversion Factor of F_lam to F_nu at 3000 A : " + str(result1)
print "Conversion Factor of F_nu to F_lam at 3000 A : " + str(result2)

conv = wave_to_freq(5500.)

test3 = flam_to_fnu(10000., 5500.)
result3 = test3 / 10000.
test4 = fnu_to_flam(test3, conv)
result4 = test4 / test3

print "Conversion Factor of F_lam to F_nu at 5500 A : " + str(result3)
print "Conversion Factor of F_nu to F_lam at 5500 A : " + str(result4)

conv = wave_to_freq(8000.)

test5= flam_to_fnu(10000., 8000.)
result5 = test5 / 10000.
test6= fnu_to_flam(test5, conv)
result6 = test6 / test5

print "Conversion Factor of F_lam to F_nu at 8000 A : " + str(result5)
print "Conversion Factor of F_nu to F_lam at 8000 A : " + str(result6)
