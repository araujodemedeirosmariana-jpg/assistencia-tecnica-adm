const API_URL = "http://localhost:8000";

async function carregarClientes() {
    const response = await fetch(`${API_URL}/clientes`);
    const clientes = await response.json();
    
    let html = '<h2>Clientes</h2><button onclick="mostrarFormCliente()">Novo Cliente</button>';
    html += '<table><tr><th>ID</th><th>Nome</th><th>Contato</th><th>Tipo</th></tr>';
    
    clientes.forEach(cliente => {
        html += `<tr>
            <td>${cliente.id}</td>
            <td>${cliente.nome}</td>
            <td>${cliente.contato || '-'}</td>
            <td>${cliente.tipo}</td>
        </tr>`;
    });
    html += '</table>';
    
    document.getElementById('conteudo').innerHTML = html;
}

async function carregarEquipamentos() {
    const response = await fetch(`${API_URL}/equipamentos`);
    const equipamentos = await response.json();
    
    let html = '<h2>Equipamentos</h2><button onclick="mostrarFormEquipamento()">Novo Equipamento</button>';
    html += '<table><tr><th>ID</th><th>Código</th><th>Tipo</th><th>Marca</th><th>Modelo</th><th>Quantidade</th></tr>';
    
    equipamentos.forEach(equip => {
        html += `<tr>
            <td>${equip.id}</td>
            <td>${equip.codigo}</td>
            <td>${equip.tipo}</td>
            <td>${equip.marca || '-'}</td>
            <td>${equip.modelo || '-'}</td>
            <td>${equip.quantidade}</td>
        </tr>`;
    });
    html += '</table>';
    
    document.getElementById('conteudo').innerHTML = html;
}

async function carregarOrdens() {
    const response = await fetch(`${API_URL}/ordens-servico`);
    const ordens = await response.json();
    
    let html = '<h2>Ordens de Serviço</h2><button onclick="mostrarFormOS()">Nova OS</button>';
    html += '<table><tr><th>ID</th><th>Cliente ID</th><th>Descrição</th><th>Status</th><th>Data Abertura</th><th>Valor Total</th></tr>';
    
    ordens.forEach(os => {
        html += `<tr>
            <td>${os.id}</td>
            <td>${os.cliente_id}</td>
            <td>${os.descricao_problema.substring(0, 50)}...</td>
            <td>${os.status}</td>
            <td>${os.data_abertura}</td>
            <td>R$ ${os.valor_total}</td>
        </tr>`;
    });
    html += '</table>';
    
    document.getElementById('conteudo').innerHTML = html;
}

function mostrarFormCliente() {
    document.getElementById('conteudo').innerHTML = `
        <h2>Novo Cliente</h2>
        <div class="form-group">
            <label>Nome:</label>
            <input type="text" id="nome">
        </div>
        <div class="form-group">
            <label>Contato:</label>
            <input type="text" id="contato">
        </div>
        <div class="form-group">
            <label>Tipo (PF/PJ):</label>
            <input type="text" id="tipo">
        </div>
        <button onclick="salvarCliente()">Salvar</button>
    `;
}

async function salvarCliente() {
    const cliente = {
        nome: document.getElementById('nome').value,
        contato: document.getElementById('contato').value,
        tipo: document.getElementById('tipo').value,
        endereco: ""
    };
    
    await fetch(`${API_URL}/clientes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(cliente)
    });
    
    carregarClientes();
}

function mostrarFormEquipamento() {
    document.getElementById('conteudo').innerHTML = `
        <h2>Novo Equipamento</h2>
        <div class="form-group">
            <label>Código:</label>
            <input type="text" id="codigo">
        </div>
        <div class="form-group">
            <label>Tipo:</label>
            <input type="text" id="tipo">
        </div>
        <div class="form-group">
            <label>Marca:</label>
            <input type="text" id="marca">
        </div>
        <div class="form-group">
            <label>Modelo:</label>
            <input type="text" id="modelo">
        </div>
        <div class="form-group">
            <label>Quantidade:</label>
            <input type="number" id="quantidade" value="1">
        </div>
        <button onclick="salvarEquipamento()">Salvar</button>
    `;
}

async function salvarEquipamento() {
    const equipamento = {
        codigo: document.getElementById('codigo').value,
        tipo: document.getElementById('tipo').value,
        marca: document.getElementById('marca').value,
        modelo: document.getElementById('modelo').value,
        quantidade: parseInt(document.getElementById('quantidade').value)
    };
    
    await fetch(`${API_URL}/equipamentos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(equipamento)
    });
    
    carregarEquipamentos();
}