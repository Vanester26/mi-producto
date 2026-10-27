# Conteo de temas: product/data/comentarios_y_feedback_real_de_usuarios_de_rm.md
# Una entrada = 1 tema principal. Criterio de alcance: parte del spec sugeridor-ajustes.
from collections import Counter, defaultdict
E = {  # id: (fuente, rol, tema, tipo)
 1:("foro","analista","recoleccion","complaint"), 2:("review","jefe","recoleccion","complaint"),
 3:("ticket","direccion","historial","complaint"), 4:("review","analista","recoleccion","usability"),
 5:("review","jefe","sugerencia","request"), 6:("mixto","analista","cobertura","complaint"),
 7:("foro","analista","ocupacion","request"), 8:("ticket","analista","sugerencia","complaint"),
 9:("review","analista","WEAK:conexiones","complaint"), 10:("ticket","jefe","recoleccion","complaint"),
 11:("review","direccion","costo","complaint"), 12:("review","jefe","razon","complaint"),
 13:("review","direccion","complejidad","complaint"), 14:("ticket","direccion","integracion","complaint"),
 15:("foro","analista","canal","complaint"), 16:("review","jefe","canal","request"),
 17:("foro","analista","ocupacion","request"), 18:("review","analista","canal","complaint"),
 19:("review","jefe","complejidad","usability"), 20:("review","otro","costo","complaint"),
 21:("ticket","analista","OUT","-"), 22:("foro","analista","integracion","usability"),
 23:("ticket","analista","historial","request"), 24:("review","jefe","OUT","-"),
 25:("ticket","analista","OUT","-"), 26:("mixto","analista","historial","complaint"),
 27:("foro","jefe","cobertura","complaint"), 28:("review","direccion","cobertura","complaint"),
 29:("ticket","analista","historial","complaint"), 30:("review","direccion","razon","request"),
}
print("n:",len(E)); print("fuentes:",Counter(v[0] for v in E.values()))
ins=[k for k,v in E.items() if v[2]!="OUT"]; print("en alcance:",len(ins),"fuera:",len(E)-len(ins))
by=defaultdict(list)
for k in ins: by[E[k][2]].append(k)
for t,ids in sorted(by.items(), key=lambda x:-len(x[1])):
    print(f"{t:14} n={len(ids)} {100*len(ids)/len(ins):.0f}% ids={ids} fuentes={dict(Counter(E[i][0] for i in ids))} roles={dict(Counter(E[i][1] for i in ids))} tipos={dict(Counter(E[i][3] for i in ids))}")
print("roles en alcance:",Counter(E[k][1] for k in ins))
