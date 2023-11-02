import numpy as np

def convertSNR(x, inputmode, outputmode, **kwargs):
    if inputmode == "ebno":
        if outputmode == "snr":
            Nbps = kwargs.get("BitsPerSymbol", 1)
            R = kwargs.get("CodingRate", 1)
            Nsps = kwargs.get("SamplesPerSymbol", 1)
            snr = x + 10 * np.log10((Nbps * R) / Nsps)
            return snr
        elif outputmode == "esno":
            Nbps = kwargs.get("BitsPerSymbol", 1)
            R = kwargs.get("CodingRate", 1)
            esno = x + 10 * np.log10(Nbps * R)
            return esno
    elif inputmode == "snr":
        if outputmode == "ebno":
            Nbps = kwargs.get("BitsPerSymbol", 1)
            R = kwargs.get("CodingRate", 1)
            Nsps = kwargs.get("SamplesPerSymbol", 1)
            ebno = x - 10 * np.log10((Nbps * R) / Nsps)
            return ebno
        elif outputmode == "esno":
            Nsps = kwargs.get("SamplesPerSymbol", 1)
            esno = x + 10 * np.log10(Nsps)
            return esno
    elif inputmode == "esno":
        if outputmode == "ebno":
            Nbps = kwargs.get("BitsPerSymbol", 1)
            R = kwargs.get("CodingRate", 1)
            ebno = x - 10 * np.log10(Nbps * R)
            return ebno
        elif outputmode == "snr":
            Nsps = kwargs.get("SamplesPerSymbol", 1)
            snr = x - 10 * np.log10(Nsps)
            return snr
    elif inputmode == "snrsc":
        if outputmode == "snr":
            NSC = kwargs.get("NumActiveSubcarriers", 1)
            FFTLen = kwargs.get("FFTLength", 1)
            snr = x + 10 * np.log10(NSC / FFTLen)
            return snr
    else:
        raise ValueError("Modo de entrada ou saída inválido")
