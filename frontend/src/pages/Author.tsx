import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Author: React.FC = () => {
  return (
    <div id="page-author-2">
    <div id="i2xrz" style={{"display": "flex", "height": "100vh", "fontFamily": "Arial, sans-serif", "--chart-color-palette": "default"}}>
      <nav id="ic61a" style={{"width": "250px", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "padding": "20px", "overflowY": "auto", "display": "flex", "flexDirection": "column", "--chart-color-palette": "default"}}>
        <h2 id="i2m23" style={{"marginTop": "0", "fontSize": "24px", "marginBottom": "30px", "fontWeight": "bold", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="igwq5" style={{"display": "flex", "flexDirection": "column", "flex": "1", "--chart-color-palette": "default"}}>
          <a id="ijuob" style={{"color": "white", "textDecoration": "none", "padding": "10px 15px", "display": "block", "background": "transparent", "borderRadius": "4px", "marginBottom": "5px", "--chart-color-palette": "default"}} href="/book">{"Book"}</a>
          <a id="ii09p" style={{"color": "white", "textDecoration": "none", "padding": "10px 15px", "display": "block", "background": "transparent", "borderRadius": "4px", "marginBottom": "5px", "--chart-color-palette": "default"}} href="/library">{"Library"}</a>
          <a id="i4hz5" style={{"color": "white", "textDecoration": "none", "padding": "10px 15px", "display": "block", "background": "rgba(255,255,255,0.2)", "borderRadius": "4px", "marginBottom": "5px", "--chart-color-palette": "default"}} href="/author">{"Author"}</a>
        </div>
        <p id="i4grx" style={{"marginTop": "auto", "paddingTop": "20px", "borderTop": "1px solid rgba(255,255,255,0.2)", "fontSize": "11px", "opacity": "0.8", "textAlign": "center", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="ib565" style={{"flex": "1", "padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default"}}>
        <h1 id="iga1t" style={{"marginTop": "0", "color": "#333", "fontSize": "32px", "marginBottom": "10px", "--chart-color-palette": "default"}}>{"Author"}</h1>
        <p id="ixlx6" style={{"color": "#666", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"Manage Author data"}</p>
        <TableBlock id="table-author-2" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Author List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Name", "column_type": "field", "field": "name", "type": "str", "required": true}, {"label": "Birth", "column_type": "field", "field": "birth", "type": "date", "required": true}, {"label": "Books", "column_type": "lookup", "path": "books", "entity": "Book", "field": "title", "type": "list", "required": false}], "formColumns": [{"column_type": "field", "field": "name", "label": "name", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "birth", "label": "birth", "type": "date", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "books", "field": "books", "lookup_field": "title", "entity": "Book", "type": "list", "required": false}]}} dataBinding={{"entity": "Author", "endpoint": "/author/"}} />
      </main>
    </div>    </div>
  );
};

export default Author;
