import { startCase } from "lodash";
import React, { useState } from "react";
import styled from "styled-components";
import { TCard, TModelBusinessCardBusinessLogic, TModelBusinessCardPrompt } from "../data/cardStore";

const BusinessLogicPanel: React.FC<{ businessLogic: TModelBusinessCardBusinessLogic }>  = ({ businessLogic }) => {
  const [isOpen, setIsOpen] = useState(true);
  return (
    <StyledCardPanel>
      <div className="prompt-panel" onClick={() => setIsOpen(!isOpen)}>
        {businessLogic.name}
      </div>
      {isOpen && (
        <div>
          <p><u>Description:</u> {businessLogic.description}</p>
          <p><u>Tags</u>: {businessLogic.tags.join(', ')}</p>
          <div>
            <u>Prompts</u>:
            <ul>
              {businessLogic.prompts.map((str) => <li key={str}>{str}</li>)}
            </ul>
          </div>
        </div>
      )}
    </StyledCardPanel>
  )
}

const PromptPanel: React.FC<{ prompt: TModelBusinessCardPrompt }> = ({ prompt }) => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <StyledCardPanel>
      <div className="prompt-panel" onClick={() => setIsOpen(!isOpen)}>
        {prompt.name}
      </div>
      {isOpen && <pre>{prompt.prompt}</pre>}
    </StyledCardPanel>
  )
}

export const RolodexCard: React.FC<{ card: TCard }> = ({ card }) => {
  // RENDER
  return (
    <StyledRolodexCard>
      <header>
        <div>
          <h1>{startCase(card.data.name)}</h1>
          <small>Models:&ensp;{card.data.models.join(', ')}</small>
        </div>
        <button>X</button>
      </header>
      <hr />
      <div>
        <h2>Business Logic</h2>
        {card.data.businessLogics.map((businessLogic) => <BusinessLogicPanel key={JSON.stringify(businessLogic)} businessLogic={businessLogic} />)}
      </div>
      <hr />
      <div>
        <h2>Prompts</h2>
        {card.data.prompts.map((prompt) => <PromptPanel key={prompt.name} prompt={prompt} />)}
      </div>
    </StyledRolodexCard>
  )
}


export const StyledRolodexCard = styled.div`
  display: flex;
  flex-direction: column;
  height: auto
  width: 100%;
  min-width: 420px;
  max-width: 420px;
  margin: 0 12px;
  padding: 12px;
  background: #fff;
  overflow: scroll;
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  h1 {
    margin: 0;
    margin-bottom: 8px;
    padding: 0;
    font-size: 18px;
    font-weight: 900;
  }
  h2 {
    margin: 0;
    margin-bottom: 8px;
    padding: 0;
    font-size: 14px;
    font-weight: 900;
  }
  hr {
    width: 100%;
    margin: 8px 0 12px;
    opacity: 0.25;
  }
  ul {
    margin: 8px 0;
    padding-left: 20px;
  }
`;

export const StyledCardPanel = styled.div`
  margin: 12px 0;
  background: #f0f0f0;
  .prompt-panel {
    padding: 4px 12px;
    font-weight: 800;
    &:hover {
      cursor: pointer;
    }
  }
  pre, & > div:not(.prompt-panel) {
    margin: 0;
    padding: 12px;
    background: #fafafa;
    overflow-x: scroll;
    font-size: 12px;
  }
  p {
    margin: 6px 0;
  }
`;
