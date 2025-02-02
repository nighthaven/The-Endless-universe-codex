import styled from 'styled-components';

export const Title = styled.div`
  color: #fd6400;
  width: 90%;
  margin-left: 100px;
  text-shadow:
    -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000;
`;

export const ImageContainerFaction = styled.div`
  width: 400px;
  height: 200px;
  flex: 1 1 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid black;
  margin: 20px 0px 15px;
  overflow: hidden;
`;

export const ImageBackground = styled.div<{ imageUrl: string }>`
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-image: ${({ imageUrl }) => `url(${imageUrl})`};
`;

export const InfoContainer = styled.div`
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  width: 90%;
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  padding: 1.5rem;
  background-color: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(253, 100, 0, 0.5);
  backdrop-filter: blur(6px);
  box-shadow: inset 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
  margin: 20px auto;

  span,
  h2,
  p {
    pointer-events: none; /* Évite les surlignements ou changements */
  }

  span {
    color: #fd6400;
    text-shadow:
      -1px -1px 0 #000,
      1px -1px 0 #000,
      -1px 1px 0 #000,
      1px 1px 0 #000;
  }

  h2 {
    color: #fd6400;
    min-width: 15%;
    margin-bottom: 10px;
    text-shadow:
      -1px -1px 0 #000,
      1px -1px 0 #000,
      -1px 1px 0 #000,
      1px 1px 0 #000;
  }

  p {
    color: #ffffff;
    font-size: 1.3rem;
  }

  &:hover {
    box-shadow: 0 4px 6px rgba(253, 100, 0, 0.3);

    ${ImageBackground} {
      transform: scale(1.1);
      transition: transform 6s cubic-bezier(0.25, 0.45, 0.45, 0.95);
    }
  }
`;

export const InfoText = styled.div`
  flex: 1;
`;

export const RightInformation = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  margin-left: 20px;

  p {
    color: #ffffff;
    font-size: 1.3rem;
    text-align: right;
  }
`;
