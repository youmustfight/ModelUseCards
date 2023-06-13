import React from "react";
import ReactDOM from "react-dom";
import styled from "styled-components";
import { Rolodex } from "./components/Rolodex";

const App: React.FC = () => {
  return (
      <Rolodex />
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
