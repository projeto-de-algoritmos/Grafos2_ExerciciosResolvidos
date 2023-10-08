/**
 * @param {number[][]} grid
 * @return {number}
 */
var swimInWater = function(grid) {
    const n = grid.length;
    
    if (n === 1) return grid[0][0];
    
    // Array para rastrear células visitadas
    const visited = Array(n).fill(false).map(() => Array(n).fill(false));
    
    // Min Heap para armazenar tempos e coordenadas
    const minHeap = new MinPriorityQueue({ priority: x => x.time });
    
    // Inicializa a fila com o ponto de partida
    minHeap.enqueue({ time: grid[0][0], row: 0, col: 0 });
    
    // Direções possíveis: direita, esquerda, baixo, cima
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    
    while (!minHeap.isEmpty()) {
        // Extrai o nó com o menor tempo da fila
        const { time, row, col } = minHeap.dequeue().element;
        
        // Se alcançarmos o destino, retorna o tempo
        if (row === n - 1 && col === n - 1) return time;
        
        // Explora as direções vizinhas
        for (const [dx, dy] of directions) {
            const nextRow = row + dx;
            const nextCol = col + dy;
            
            // Verifica se a próxima coordenada está dentro dos limites e não foi visitada
            if (nextRow < 0 || nextCol < 0 || nextRow >= n || nextCol >= n || visited[nextRow][nextCol]) continue;
            
            // Marca a célula como visitada
            visited[nextRow][nextCol] = true;
            
            // Adiciona a próxima célula à fila com o tempo máximo entre o tempo atual e o tempo da próxima célula
            minHeap.enqueue({ time: Math.max(time, grid[nextRow][nextCol]), row: nextRow, col: nextCol });
        }
    }
};
