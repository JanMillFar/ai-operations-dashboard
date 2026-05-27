def generar_recomendacion(riesgo):

    if riesgo == "ALTO":
        return "Revisar proveedores críticos y priorizar entregas urgentes."

    elif riesgo == "MEDIO":
        return "Monitorizar incidencias y revisar tiempos de entrega."

    else:
        return "Operativa estable."