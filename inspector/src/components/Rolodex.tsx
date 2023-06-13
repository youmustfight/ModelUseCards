import React, { useState } from "react";
import styled from "styled-components";
import { RolodexCard, StyledRolodexCard } from "./RolodexCard";
import { useCardStore } from "../data/cardStore";
import { RolodexCardAdder } from "./RolodexCardAdder";


export const Rolodex = () => {
  const { cards } = useCardStore();
  
  // RENDER
  return (
    <StyledRolodex>
      <main>
        <RolodexCardAdder />
        {cards.map((card) => (
          <RolodexCard key={card.sourceUrl} card={card} />
        ))}
      </main>
    </StyledRolodex>
  )
}

const StyledRolodex = styled.div`
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  background: #eee;
  * {
    font-family: 'Lato', sans-serif;
    font-weight: 400;
    box-sizing: border-box;
    font-size: 13px;
  }
  main {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-grow: 1;
    padding: 12px;
  }
`;
