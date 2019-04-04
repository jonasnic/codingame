(ns Player
  (:gen-class))

(defn -main [& args]
  (while true
    (let [
      heights (repeatedly 8 read)
      max (apply max heights)
      indexMax (.indexOf heights max)]

    ; The index of the mountain to fire on.
    (println indexMax))))
