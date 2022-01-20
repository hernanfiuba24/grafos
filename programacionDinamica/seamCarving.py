(i,j)=pixel (i,j) en la grilla

OPT[i,j] = M[i,j], para j=1 (primer columna)
OPT[i,j]=Min(*){OPT[pixel]} + M[i,j], * pixeles anteriores a (i,j) validos

seamCarving(M):
    OPT[][] matriz de tamanio W*H
    inicializo OPT en +INF

    // Caso base
    Para cada i de 0 a W-1:     // Recorro filas de primer columna
        OPT[i,0] = M[i,0]
    
    

    Para cada i de 1 a H-1: // Tomo a partir de la segunda columna
        
        Para cada j de 0 a W-1:      // Recorro filas

            minPixelAnterior = +INF

            if (OPT[i-1, j-1] < minPixelAnterior):    // Si es sea primer fila
                minPixelAnterior = OPT[i-1, j-1]
            if (OPT[i, j-1] < minPixelAnterior):
                minPixelAnterior = OPT[i, j-1]
            if (OPT[i+1, j-1] < minPixelAnterior):    // Y si no es ultima fila
                minPixelAnterior = OPT[i+1, j-1]

            OPT[i,j] = minPixelAnterior + M[i,j]

    minEnergia = +INF
    pixelOpt = NULL
    Para cada i de 0 a W-1: // Recorro filas de ultima columna
        Si OPT[i, H-1] < minEnergia:
            minEnergia = OPT[i, H-1]
            pixelOpt = (i, H-1)

    minPixelAnterior = +INF
    Mientras pixelOpt.y >= 0:
        imprimir pixelOpt

        if OPT[pixelOpt.i-1, pixelOpt.j-1] < minPixelAnterior):    // Si es sea primer fila
            pixelOpt = pixelOpt.i-1, pixelOpt.j-1
            minPixelAnterior = OPT[pixelOpt.i-1, pixelOpt.j-1]
        if OPT[pixelOpt.i, pixelOpt.j-1] < minPixelAnterior):
            pixelOpt = pixelOpt.i, pixelOpt.j-1
            minPixelAnterior = OPT[pixelOpt.i, pixelOpt.j-1]
        if OPT[pixelOpt.i+1, pixelOpt.j-1] < minPixelAnterior):    // Y si no es ultima fila
            pixelOpt = pixelOpt.i+1, pixelOpt.j-1
            minPixelAnterior = OPT[pixelOpt.i+1, pixelOpt.j-1]


