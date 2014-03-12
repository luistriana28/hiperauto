## -*- coding: utf-8 -*-
<html>
<head>
    <style type="text/css">
        ${css}

.list_main_table {
    border:thin solid #E3E4EA;
    text-align:center;
    border-collapse: collapse;
}
table.list_main_table {
    margin-top: 20px;
}
.list_main_headers {
    padding: 0;
}
.list_main_headers th {
    border: thin solid #000000;
    padding-right:3px;
    padding-left:3px;
    background-color: #EEEEEE;
    text-align:center;
    font-size:12;
    font-weight:bold;
}
.list_main_table td {
    padding-right:3px;
    padding-left:3px;
    padding-top:3px;
    padding-bottom:3px;
}
.list_main_lines,
.list_main_footers {
    padding: 0;
}
.list_main_footers {
    padding-top: 15px;
}
.list_main_lines td,
.list_main_footers td,
.list_main_footers th {
    border-style: none;
    text-align:left;
    font-size:12;
    padding:0;
}
.list_main_footers th {
    text-align:right;
}

td .total_empty_cell {
    width: 77%;
}
td .total_sum_cell {
    width: 13%;
}

.nobreak {
    page-break-inside: avoid;
}
caption.formatted_note {
    text-align:left;
    border-right:thin solid #EEEEEE;
    border-left:thin solid #EEEEEE;
    border-top:thin solid #EEEEEE;
    padding-left:10px;
    font-size:11;
    caption-side: bottom;
}
caption.formatted_note p {
    margin: 0;
}

.main_col1 {
    width: 40%;
}
td.main_col1 {
    text-align:left;
}
.main_col2,
.main_col3,
.main_col4,
.main_col6 {
    width: 10%;
}
.main_col5 {
    width: 7%;
}
td.main_col5 {
    text-align: center;
    font-style:italic;
    font-size: 10;
}
.main_col7 {
    width: 13%;
}

.right_table {
    right: 4cm;
    width:"100%";
}

.std_text {
    font-size:12;
}

th.date {
    width: 90px;
}

td.amount, th.amount {
    text-align: right;
    white-space: nowrap;
}

td.date {
    white-space: nowrap;
    width: 90px;
}

.address .recipient .shipping .invoice {
    font-size: 12px;
}

    </style>
</head>
<body>
    <%page expression_filter="entity"/>
    <%
    def carriage_returns(text):
        return text.replace('\n', '<br />')
    %>

    <%def name="address(partner)">
        <%doc>
            XXX add a helper for address in report_webkit module as this won''t be suported in v8.0
        </%doc>
        %if partner.parent_id:
            <tr><td class="name">${partner.parent_id.name or ''}</td></tr>
            <tr><td>${partner.title and partner.title.name or ''} ${partner.name}</td></tr>
            <% address_lines = partner.contact_address.split("\n")[1:] %>
        %else:
            <tr><td class="name">${partner.title and partner.title.name or ''} ${partner.name}</td></tr>
            <% address_lines = partner.contact_address.split("\n") %>
        %endif
        %for part in address_lines:
            % if part:
                <tr><td>${part}</td></tr>
            % endif
        %endfor
    </%def>

    %for order in objects:
    <% setLang(order.partner_id.lang) %>
    <%
      quotation = order.state in ['draft', 'sent']
    %>
    <div class="address">
    <table class="shipping">
          <tr><td class="address_title">${_("Cliente:")}</td></tr>
          ${address(partner=order.partner_shipping_id)}
    </table>
    </div>    
    <h1 style="clear:both;">${quotation and _(u'N° de Cotización') or _(u'Número de Orden°') } ${order.name}</h1>
    <h2>${_('Datos del Vehículo')}</h2>
    <table class="list_main_table" width="100%">
        <tr>
            <td>${_("Vehículo / Placas:")}</td>
            <td>${order.vehicle_id.name}</td>
            <td>${_("Número de serie:")}</td>
            <td>${order.vehicle_id.vin_sn_custom}</td>
    </table>
    %if quotation:
    <table class="list_main_table" width="100%">
        <tr>
            <td>${_("Antena")}</td>
            %if order.antena:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Llanta de refacción")}</td>
            %if order.refaccion:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Extinguidor")}</td>
            %if order.extinguidor:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Nivel de combustible")}</td>
            <td>${order.nivel_combustible}</td>
        </tr>
        <tr>
            <td>${_("Autoestéreo")}</td>
            %if order.autoestereo:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Llave o maneral")}</td>
            %if order.maneral:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Gato")}</td>
            %if order.gato:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Tapon de gasolina")}</td>
            %if order.tapon_gasolina:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
        </tr>
        <tr>
            <td>${_("Birlo de seguridad")}</td>
            %if order.birlo:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Radio de comunicación")}</td>
            %if order.radio:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Herramienta")}</td>
            %if order.herramienta:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Tapon de ruedas")}</td>
            %if order.tapon_ruedas:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
        </tr>
        <tr>
            <td>${_("Cables pasacorriente")}</td>
            %if order.pasacorriente:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Señales")}</td>
            %if order.senales:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Limpiadores")}</td>
            %if order.limpiadores:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Otro")}</td>
            <td>${order.otro}</td>
        </tr>
        <tr>
            <td>${_("Espejos laterales")}</td>
            %if order.espejos_laterales:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_("Tapetes")}</td>
            %if order.tapetes:
            <td>${_("☑")}</td>
            %else:
            <td>${_("☐")}</td>
            %endif
            <td>${_(" ")}</td>
            <td>${_(" ")}</td>
            <td>${_(" ")}</td>
            <td>${_(" ")}</td>
        </tr>
    </table>
    %endif
<br></br>
    <table class="basic_table" width="100%">
        <tr>
            <th class="date">${quotation and _("Fecha de la orden") or _("Fecha de cotización")}</td>
            <th>${_("Referencia")}</td>
            <th>${_("Vendedor")}</td>
            <th>${_('Términos de pago')}</td>
        </tr>
        <tr>
            <td class="date">${formatLang(order.date_order, date=True)}</td>
            <td>${order.client_order_ref or ''}</td>
            <td>${order.user_id and order.user_id.name or ''}</td>
            <td>${order.payment_term and order.payment_term.note or ''}</td>
        </tr>
    </table>

    <div>
    %if order.note1:
        <p class="std_text"> ${order.note1 | n} </p>
    %endif
    </div>

    <table class="list_main_table" width="100%">
      <thead>
        <tr>
          <th class="list_main_headers" style="width: 100%">
            <table style="width:100%">
              <tr>
                <th class="main_col1">${_("Descripción")}</th>
                <th class="amount main_col2">${_("Cantidad")}</th>
                <th class="amount main_col3">${_("UdM")}</th>
                <th class="amount main_col4">${_("Precio Unitario")}</th>
                <th class="main_col5">${_("IVA")}</th>
                <th class="amount main_col6">${_("Desc.(%)")}</th>
                <th class="amount main_col7">${_("Precio")}</th>
              </tr>
            </table>
          </th>
        </tr>
      </thead>
      <tbody>
        %for line in order.order_line:
          <tr>
            <td class="list_main_lines" style="width: 100%">
              <div class="nobreak">
                <table style="width:100%">
                  <tr>
                    <td class="main_col1">${ line.name }</td>
                    <td class="amount main_col2">${ formatLang(line.product_uos and line.product_uos_qty or line.product_uom_qty) }</td>
                    <td class="amount main_col3">${ line.product_uos and line.product_uos.name or line.product_uom.name }</td>
                    <td class="amount main_col4">${formatLang(line.price_unit)}</td>
                    <td class="main_col5">${ ', '.join([tax.description or tax.name for tax in line.tax_id]) }</td>
                    <td class="amount main_col6">${line.discount and formatLang(line.discount, digits=get_digits(dp='Sale Price')) or ''} ${line.discount and '%' or ''}</td>
                    <td class="amount main_col7">${formatLang(line.price_subtotal, digits=get_digits(dp='Sale Price'))}&nbsp;${order.pricelist_id.currency_id.symbol}</td>
                  </tr>
                  %if line.formatted_note:
                    <caption class="formatted_note">
                      ${line.formatted_note| n}
                    </caption>
                  %endif
                </table>
              </div>
            </td>
          </tr>
        %endfor
      </tbody>
      <tfoot class="totals">
        <tr>
          <td class="list_main_footers" style="width: 100%">
            <div class="nobreak">
              <table style="width:100%">
                <tr>
                  <td class="total_empty_cell"/>
                  <th>
                    ${_("Total Neto:")}
                  </th>
                  <td class="amount total_sum_cell">
                    ${formatLang(order.amount_untaxed, get_digits(dp='Sale Price'))} ${order.pricelist_id.currency_id.symbol}
                  </td>
                </tr>
                <tr>
                  <td class="total_empty_cell"/>
                  <th>
                    ${_("Impuestos:")}
                  </th>
                  <td class="amount total_sum_cell">
                    ${formatLang(order.amount_tax, get_digits(dp='Sale Price'))} ${order.pricelist_id.currency_id.symbol}
                  </td>
                </tr>
                <tr>
                  <td class="total_empty_cell"/>
                  <th>
                    ${_("Total:")}
                  </th>
                  <td class="amount total_sum_cell">
                    <b>${formatLang(order.amount_total, get_digits(dp='Sale Price'))} ${order.pricelist_id.currency_id.symbol}</b>
                  </td>
                </tr>
              </table>
            </div>
          </td>
        </tr>
      </tfoot>
    </table>

    %if order.note :
        <p class="std_text">${order.note | carriage_returns}</p>
    %endif
    %if order.note2:
        <p class="std_text">${order.note2 | n}</p>
    %endif
    <p style="page-break-after:always"/>
    %endfor
</body>
</html>