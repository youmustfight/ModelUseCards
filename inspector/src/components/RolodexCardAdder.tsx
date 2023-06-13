import React, { useState } from 'react';
import { useCardStore } from '../data/cardStore';
import { StyledRolodexCard } from './RolodexCard';
import { exampleMBCSourceUrls } from '../data/mbc';
import styled from 'styled-components';

export const RolodexCardAdder = () => {
  const [selectedUrl, setSelectedUrl] = useState("");
  const { addCard } = useCardStore();
  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Add card & reset input
    if (selectedUrl) {
      addCard(selectedUrl);
      setSelectedUrl("");
    }
  }
  
  // RENDER
  return (
      <StyledRolodexCardAdder>
        <header>
          <h1>Model Business Cards</h1>
        </header>
        <hr />
        <form onSubmit={onSubmit}>
          <p>Select an example:</p>
          <select value={selectedUrl} onChange={e => setSelectedUrl(e.target.value)}>
            <option value="">---</option>
            {exampleMBCSourceUrls.map((url) => (
              <option key={url} value={url}>{url}</option>
            ))}
          </select>
          <p>or enter a URL:</p>
          <input type="text" value={selectedUrl} onChange={e => setSelectedUrl(e.target.value)} />
          <hr />
          <button type="submit">Load an App MBC</button>
        </form>
      </StyledRolodexCardAdder>
  )
}

const StyledRolodexCardAdder = styled(StyledRolodexCard)`
  width: 280px;
  min-width: 280px;
  max-width: 280px;
  background: rgba(255,255,255,0.3);
  form {
    display: flex;
    flex-direction: column;
  }
`;
