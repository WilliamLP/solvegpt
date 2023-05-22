



TARGET = 2000000
best_rect, best_score = None, TARGET
for h in range(1, TARGET):
    h_segs = h * (h + 1) // 2
    if h_segs ** 2 >= TARGET + best_score:
        break
    for w in range(h, TARGET):
        w_segs = w * (w + 1) // 2
        score = abs(w_segs * h_segs - TARGET)
        if score < best_score:
            best_rect, best_score = (w, h), score
        if score >= TARGET + best_score:
            break
print(best_rect, best_rect[0] * best_rect[1], best_score)