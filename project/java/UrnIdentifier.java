package None;

import java.util.List;
import lombok.*;






/**
  A URN (Uniform Resource Name).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UrnIdentifier extends RelatedIdentifier {

  private String identifier;

}
